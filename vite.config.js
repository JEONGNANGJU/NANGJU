import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  base: './', // 또는 "/NANGJU/" → Vercel에서는 "./"이 일반적
  plugins: [react()],
})
