FROM node:24.20.0-alpine@sha256:e67514e5d0f6c46656005e1b693b2ec9d52e80b641307de684d4a015ba7a4eaf AS dependencies

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM dependencies AS build

COPY . .
RUN npm run check && npm run build && npm prune --omit=dev

FROM node:24.20.0-alpine@sha256:e67514e5d0f6c46656005e1b693b2ec9d52e80b641307de684d4a015ba7a4eaf AS runtime

ENV HOST=0.0.0.0
ENV PORT=3000
ENV NODE_ENV=production

RUN addgroup -S -g 10001 ibm && adduser -S -D -H -u 10001 -G ibm ibm

WORKDIR /app
COPY --from=build --chown=10001:10001 /app/build ./build
COPY --from=build --chown=10001:10001 /app/node_modules ./node_modules
COPY --from=build --chown=10001:10001 /app/package.json ./package.json

EXPOSE 3000
USER 10001:10001
CMD ["node", "build"]
