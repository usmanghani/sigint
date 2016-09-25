import { combineReducers } from 'redux'

import { RECEIVE_FILE, RECEIVE_DATA_URL } from '../actions'


function file(state = null, action) {
  switch (action.type) {
    case RECEIVE_FILE:
      return action.file
    default:
      return state
  }
}

function dataUrl(state = '', action) {
  switch (action.type) {
    case RECEIVE_DATA_URL:
      return action.dataUrl
    default:
      return state
  }
}

const rootReducer = combineReducers({
  file,
  dataUrl,
})

export default rootReducer
