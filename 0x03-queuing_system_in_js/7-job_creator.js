import kue from 'kue'
const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

jobs.forEach(job => {
  const newJob = queue.create('push_notification_code_2', job)
    .save(err => {
      if (err) {
        console.error(`Notification job failed: ${err}`);
      } else {
        console.log(`Notification job created: ${newJob.id}`);

        newJob
          .on('complete', () => {
            console.log(`Notification job ${newJob.id} completed`);
          })
          .on('failed', err => {
            console.log(`Notification job ${newJob.id} failed: ${err}`);
          })
          .on('progress', (progress, data) => {
            console.log(`Notification job ${newJob.id} ${progress}% complete`);
          });
      }
    });
});


process.once('SIGTERM', sig => {
  queue.shutdown(5000, err => {
    console.log('Kue shutdown: ', err || '');
    process.exit(0);
  });
});