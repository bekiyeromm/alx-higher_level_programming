#!/usr/bin/node
const dict = require('./101-data.js').dict;
function getUserIdsByOccurrence (dict) {
  const result = {};
  // Iterate over the user ids in the input dictionary
  for (const userId in dict) {
    const occurrence = dict[userId];
    // Add the user id to the list of ids for this occurrence count
    if (!result[occurrence]) {
      result[occurrence] = [];
    }
    result[occurrence].push(userId);
  }
  return result;
}
const userIdsByOccurrence = getUserIdsByOccurrence(dict);
console.log(userIdsByOccurrence);
