import fetch from 'isomorphic-fetch';
import querystring from 'querystring';

export const RECEIVE_FILE = 'RECEIVE_FILE'
export const RECEIVE_DATA_URL = 'RECEIVE_DATA_URL'


export function receiveFile(file) {
  return {
    type: RECEIVE_FILE,
    file
  }
}

export function receiveDataUrl(dataUrl) {
  return {
    type: RECEIVE_DATA_URL,
    dataUrl
  }
}

export function loadFile(file) {
  return dispatch => {
    dispatch(receiveFile(file))
    const freader = new FileReader();
    freader.onload = function(e) {
      dispatch(receiveDataUrl(e.target.result));
    }
    freader.readAsDataURL(file)
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
