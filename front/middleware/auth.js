export default function ({ store: { getters }, route: { path }, redirect }) {

  const userIsLoggedIn = getters['users/isAuth']; // #true = пользователь авторизован || #false = пользователь не авторизован

  if (!userIsLoggedIn) {
    redirect({name: 'user-login'}, {redirect: path})
  }

}
