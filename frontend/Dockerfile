# Dockerfile for Frontend (Next.js)
FROM node:18-alpine AS builder
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

FROM node:18-alpine AS runner
WORKDIR /app
COPY --from=builder /app .
CMD ["npm", "run", "start"]