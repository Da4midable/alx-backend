import { createClient } from 'redis';
import { promisify } from 'util';


const client = createClient();


const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);


client.on('connect', async () => {
    console.log('Redis client connected to the server');

    try {
        await setAsync('Holberton', 'School');
        console.log('Key set successfully');
        const value = await getAsync('Holberton');
        console.log(`${value}`);
    } catch (err) {
        console.error(`Error: ${err.message}`);
    } finally {
        client.quit();
    }
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
