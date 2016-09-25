import { combineReducers } from 'redux'

import { RECEIVE_FILE, RECEIVE_DATA_URL, RECIEVE_PLAYER_TIME } from '../actions'


function playerInfo(state = {}, action) {
  switch (action.type) {
    case RECEIVE_FILE:
      return Object.assign({}, state, {file: action.file})
    case RECEIVE_DATA_URL:
      return Object.assign({}, state, {dataUrl: action.dataUrl})
    case RECIEVE_PLAYER_TIME:
      return Object.assign({}, state, {time: action.time})
    default:
      return state
  }
}


const rootReducer = combineReducers({
  playerInfo,
})

export default rootReducer
