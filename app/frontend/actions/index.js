import fetch from 'isomorphic-fetch';
import querystring from 'querystring';

export const RECEIVE_CONFIG = 'RECEIVE_CONFIG'


export function receiveConfig(config) {
  return {
    type: RECEIVE_CONFIG,
    config
  }
}

// export function getConfig() {
//   let url = ``;
//
//   return dispatch => {
//     return fetch(url)
//       .then(response => response.json())
//       .then(json => {
//         console.log(json)
//         dispatch(receiveConfig(json));
//       })
//   }
// }

// export function myAsyncAction2(actionData) {
//   return (dispatch, getState) => {
//     let state = getState();
//     return dispatch(mySyncAction2(actionData))
//   }
// }
