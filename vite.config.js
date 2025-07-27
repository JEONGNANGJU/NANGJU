import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist', // 중요! Vercel이 이 폴더를 배포 폴더로 씀
  },
  base: './' // 상대 경로로 해줘야 index.html 등 참조됨
})
