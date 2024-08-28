import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Connect the client to the Redis server
(async () => {
  try {
    await client.connect();
  } catch (err) {
    console.error('Error connecting to Redis server:', err);
  }
})();
