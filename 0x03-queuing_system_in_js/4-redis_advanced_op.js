import { createClient, print } from 'redis';

//Create a Redis client.
const client = createClient();

//Event listener for connection errors.
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

/* Update a field in a Redis hash.
 
 * @param {string} hashName - The name of the hash.
 * @param {string} fieldName - The name of the field.
 * @param {string|number} fieldValue - The value of the field.
 */
const updateHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

/**
 * Print all fields and values of a Redis hash.
 *
 * @param {string} hashName - The name of the hash.
 */
const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => {
    if (_err) {
      console.error('Error retrieving hash:', _err);
    } else {
      console.log(reply);
    }
  });
};

//Main function to update and print a Redis hash.
 
function main() {
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value);
  }

  // Ensure we wait for the HSET operations to complete before calling HGETALL
  // Add a delay to allow all HSET operations to finish
  setTimeout(() => {
    printHash('HolbertonSchools');
  }, 1000);
}

// Event listener for successful connection.
client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
