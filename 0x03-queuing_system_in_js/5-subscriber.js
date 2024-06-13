import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Exit message constant
const EXIT_MSG = 'KILL_SERVER';

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
 * Event listener for successful connection.
 * Logs a success message when the Redis client connects to the server.
 */
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

/**
 * Subscribe to the 'holberton school channel'.
 */
client.subscribe('holberton school channel');

/**
 * Event listener for messages on the subscribed channel.
 * Logs the message received from the channel. If the message is 'KILL_SERVER',
 * it unsubscribes from the channel and quits the Redis client.
 *
 * @param {string} _err - Error message placeholder (not used).
 * @param {string} msg - The message received from the channel.
 */
client.on('message', (_err, msg) => {
  console.log(msg);
  if (msg === EXIT_MSG) {
    client.unsubscribe();
    client.quit();
  }
});
