import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
})

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
})


function setNewSchool(schoolName, value, callback) {
    client.set(schoolName, value, (err, reply) => {
        print(err, reply);
        if (callback) callback();
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(`Error retrieving key: ${err}`);
        } else if (reply) {
            console.log(`${reply}`);
        } else {
            console.log(`${schoolName}: Key does not exist`);
        }
    });
}

setNewSchool('Holberton', 'School');
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
