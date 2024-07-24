import { fileURLToPath, URL } from 'node:url'
import path from 'node:path'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  root: path.join(__dirname, './spas/'),
  base: '/',
  build: {
    manifest: 'manifest.json',
    assetsDir: 'bundles',
    outDir: path.join(__dirname, './dist'),
    rollupOptions: {
      input: ['spas/main.ts', 'spas/admin.ts']
    },
    copyPublicDir: false,
    emptyOutDir: true
  },
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./spas', import.meta.url))
    }
  }
})
