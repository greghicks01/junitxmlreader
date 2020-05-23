import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
	thresholds:{
	'http_req_blocked':['p(95)<10'],
    'http_req_connecting':['p(95)<500'],
    'http_req_duration':['p(95)<10'],
    'http_req_receiving':['p(95)<500'],
    'http_req_sending':['p(95)<500'],
    'http_req_tls_handshaking':['p(95)<800'],
    'http_req_waiting':['p(95)<500'],
    'iteration_duration':['p(95)<2500']
	}
}

export default function() {
  // http.get(`${__ENV.TARGET_URL}`);
  http.get('http://test.k6.io')
  sleep(1);
}
