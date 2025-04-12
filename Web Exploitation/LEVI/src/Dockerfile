# Use the official PHP image with Apache
FROM php:8.2-apache

# Set the working directory
WORKDIR /var/www/html

# Copy the application files
COPY app/ /var/www/html/
COPY flag.txt /flag
RUN chmod 444 /flag
# Expose port 80
EXPOSE 80