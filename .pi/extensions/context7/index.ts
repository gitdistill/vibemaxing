import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Type } from "@sinclair/typebox";
import fs from "node:fs";
import path from "node:path";

export default function (pi: ExtensionAPI) {
  let mcpClient: Client | null = null;
  let transport: StdioClientTransport | null = null;

  async function ensureConnected(ctx: any) {
    if (mcpClient) return mcpClient;

    let apiKey = process.env.CONTEXT7_API_KEY;
    if (!apiKey) {
      try {
        const envPath = path.join(ctx.cwd, ".env");
        if (fs.existsSync(envPath)) {
          const envContent = fs.readFileSync(envPath, "utf-8");
          const match = envContent.match(/^CONTEXT7_API_KEY=(.*)$/m);
          if (match) {
            apiKey = match[1].replace(/["']/g, "").trim();
          }
        }
      } catch (e) {}
    }

    transport = new StdioClientTransport({
      command: "npx",
      args: ["-y", "@upstash/context7-mcp"],
      env: { ...process.env, CONTEXT7_API_KEY: apiKey || "" }
    });

    mcpClient = new Client(
      { name: "pi-context7-bridge", version: "1.0.0" },
      { capabilities: {} }
    );

    await mcpClient.connect(transport);
    return mcpClient;
  }

  // Register tools IMMEDIATELY so they are visible to Pi at boot
  pi.registerTool({
    name: "context7_resolve_library_id",
    label: "Context7: Resolve Library",
    description: "Resolves a general library name into a Context7-compatible library ID.",
    parameters: Type.Object({
      libraryName: Type.String({ description: "The name of the library to search for" }),
      query: Type.String({ description: "The user's question or task" }),
    }),
    async execute(_id, params, _sig, _upd, ctx) {
      const client = await ensureConnected(ctx);
      const result = await client.callTool({
        name: "resolve-library-id",
        arguments: params
      });
      return { content: result.content as any, isError: !!result.isError };
    }
  });

  pi.registerTool({
    name: "context7_query_docs",
    label: "Context7: Query Docs",
    description: "Retrieves documentation for a library using a Context7 library ID.",
    parameters: Type.Object({
      libraryId: Type.String({ description: "Exact Context7-compatible library ID (e.g., /mongodb/docs, /vercel/next.js)" }),
      query: Type.String({ description: "The question or task to get relevant documentation for" }),
    }),
    async execute(_id, params, _sig, _upd, ctx) {
      const client = await ensureConnected(ctx);
      const result = await client.callTool({
        name: "query-docs",
        arguments: params
      });
      return { content: result.content as any, isError: !!result.isError };
    }
  });

  pi.on("session_shutdown", async () => {
    if (mcpClient) {
      await mcpClient.close();
      mcpClient = null;
    }
  });
}
