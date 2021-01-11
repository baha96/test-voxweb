export const state = () => {
  return {
    user: null
  }
};

export const getters = {
  user(state) {
    return state.user
  },
  isAuth(state) {
    return !!state.user
  },
};

export const mutations = {
  SET_USER(state, user) {
    state.user = user
  },
};
