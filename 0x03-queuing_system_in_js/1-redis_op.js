import { createClient, print } from 'redis';

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

// Function to set a new school in Redis
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

// Function to display the value of a school from Redis
const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
