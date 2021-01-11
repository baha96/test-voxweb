export const actions = {
  async nuxtServerInit({ dispatch }) {
    try {
      await dispatch('users/getUser');
    } catch (error) {
      console.log('Not user')
    }
  },
};
