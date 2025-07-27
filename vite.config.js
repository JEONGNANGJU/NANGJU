// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  base: "./", // ← 이 부분이 핵심!
  plugins: [react()],
})
