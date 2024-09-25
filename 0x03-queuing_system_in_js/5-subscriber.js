import { createClient, print } from 'redis';


const client = createClient();


client.subscribe('holberton school');


client.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
