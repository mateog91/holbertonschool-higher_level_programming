#!/usr/bin/node
/** Function that returns number of occurances in list */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(element => {
    if (searchElement === element) {
      count++;
    }
  });
  return count;
};
