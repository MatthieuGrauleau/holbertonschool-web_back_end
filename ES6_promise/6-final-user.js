import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userpromise = signUpUser(firstName, lastName);
  const photopromise = uploadPhoto(fileName);
  const results = await Promise.allSettled([userpromise, photopromise]);

  return results.map((result) => {
    if (result.status === 'fulfilled') {
      return {
        status: 'fulfilled',
        value: result.value,
      };
    }
    return {
      status: 'rejected',
      value: result.reason,
    };
  });
}
