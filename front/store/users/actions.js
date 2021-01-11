import Cookies from 'js-cookie'

export default {
  async getUser ({commit}, data) {
    try {
      const response = await this.$axios.$get('/api/v1/account/get/user/');
      if (response) commit('SET_USER', response);
    } catch (error) {
      throw error
    }
  },
}
