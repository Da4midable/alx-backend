import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Handle connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle error event
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish a message after a delay
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school', message);
  }, time);
}

// Call publishMessage with different delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
