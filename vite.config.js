import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  base: './', // 로컬과 Vercel에서 모두 동작하게
  plugins: [react()],
})
