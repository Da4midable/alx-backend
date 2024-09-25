import kue from 'kue';
const queue = kue.createQueue();

const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach(job => {
        const newJob = queue.create('push_notification_code_3', {
            phoneNumber: job.phoneNumber,
            message: job.message
        })
        .save(err => {
            if (err) {
                console.error(`Notification job ${newJob.id} failed: ${err}`);
            } else {
                console.log(`Notification job created: ${newJob.id}`);

                newJob
                    .on('complete', () => {
                        console.log(`Notification job ${newJob.id} completed`);
                    })
                    .on('failed', err => {
                        console.error(`Notification job ${newJob.id} failed: ${err}`);
                    })
                    .on('progress', (progress, data) => {
                        console.log(`Notification job ${newJob.id} ${progress}% complete`);
                    });
            }
        });
    });
};

export default createPushNotificationsJobs;
