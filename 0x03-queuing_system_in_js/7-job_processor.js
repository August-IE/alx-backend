import { createQueue, Job } from 'kue';

// List of blacklisted phone numbers
const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];

// Create a job queue for push notifications
const queue = createQueue();

/**
 * Sends a push notification to a user.
 *
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to send.
 * @param {Job} job - The job object representing the notification task.
 * @param {Function} done - The callback to call when the job is done.
 */
const sendNotification = (phoneNumber, message, job, done) => {
  let total = 2;
  let pending = 2;
  const sendInterval = setInterval(() => {
    if (total - pending <= total / 2) {
      job.progress(total - pending, total);
    }

    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }

    if (total === pending) {
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    }

    --pending || done();
    pending || clearInterval(sendInterval);
  }, 1000);
};

/**
 * Process the 'push_notification_code_2' jobs from the queue.
 * 
 * @param {Job} job - The job object representing the notification task.
 * @param {Function} done - The callback to call when the job is done.
 */
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
