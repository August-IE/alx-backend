import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

/**
 * Event listener for connection errors.
 * Logs an error message if the Redis client cannot connect to the server.
 *
 * @param {Error} err - The error object containing the connection error details.
 */
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

/**
 * Publish a message to the 'holberton school channel' after a specified delay.
 *
 * @param {string} message - The message to be published.
 * @param {number} time - The delay in milliseconds before publishing the message.
 */
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
};

/**
 * Event listener for successful connection.
 * Logs a success message when the Redis client connects to the server.
 */
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

/**
 * Publish several messages to the 'holberton school channel' with varying delays.
 */
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
