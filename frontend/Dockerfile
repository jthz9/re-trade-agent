# Stage 1: Build the Next.js application
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and yarn.lock
COPY package.json yarn.lock ./
# If using yarn, uncomment the next line and comment out the npm ci line
# COPY yarn.lock ./

# Install dependencies
# RUN npm ci
RUN yarn install --frozen-lockfile
# If using yarn, uncomment the next line and comment out the npm ci line
# RUN yarn install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Create .next and public directories if they don't exist, before build
RUN mkdir -p .next public

# Build the Next.js application
# RUN npm run build
RUN yarn build
# If using yarn, uncomment the next line and comment out the npm run build line
# RUN yarn build

# Stage 2: Serve the Next.js application
FROM node:18-alpine

WORKDIR /app

# Copy built assets from the builder stage
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/yarn.lock ./yarn.lock
# If you have a custom server, copy it as well
# COPY --from=builder /app/server.js ./server.js

# Install production dependencies (if any, Next.js standalone output handles this often)
# RUN npm ci --only=production
# If using yarn, uncomment the next line and comment out the npm ci line
# RUN yarn install --production --frozen-lockfile

# Expose port
EXPOSE 3000

# Command to run the application
# CMD ["npm", "start"]
# CMD ["yarn", "start"] # JSON array format
CMD yarn start
# If using yarn, uncomment the next line and comment out the npm start line
# CMD ["yarn", "start"]
