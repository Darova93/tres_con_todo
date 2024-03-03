import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { UserConfig } from "vitest/config";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    test: {
        globals: true,
        environment: "jsdom",
    },
    server: {
        port: 3000,
    },
}) as UserConfig;
