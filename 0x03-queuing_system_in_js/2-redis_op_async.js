import { createClient, print } from 'redis';
import { promisify } from 'util';

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

// Function to set a new school in Redis
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

// Promisify the client.get method
const getAsync = promisify(client.get).bind(client);

// Async function to display the value of a school from Redis
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error('Error retrieving value:', err);
  }
}

// Connect the client to the Redis server
(async () => {
  try {
    await client.connect();

    // Call the functions as required
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  } catch (err) {
    console.error('Error connecting to Redis server:', err);
  }
})();
