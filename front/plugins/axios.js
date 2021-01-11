import Cookies from 'js-cookie'
export default function ({$axios}) {
  $axios.setHeader('X-CSRFTOKEN', Cookies.get('csrftoken'));
  $axios.onRequest(() => {
    $axios.setHeader('X-CSRFTOKEN', Cookies.get('csrftoken'));
  });
}
