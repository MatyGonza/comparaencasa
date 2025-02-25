# The first stage
# Build React static files
FROM node:18-alpine AS build

WORKDIR /app
# Copiar configuración personalizada
COPY ./frontend/package.json ./frontend/package-lock.json ./
RUN npm install --silent
COPY ./frontend/src ./src
COPY ./frontend/public ./public
COPY ./frontend/webpack.config.js ./
COPY ./frontend/.babelrc ./
RUN npm run build
#COPY ./frontend/build ./build

# The second stage
# Copy React static files and start nginx
FROM nginx:stable-alpine
COPY ./docker/nginx/development/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
COPY --from=build /app/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]