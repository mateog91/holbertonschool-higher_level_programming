#!/usr/bin/node
function converter(base) {
  return function (number) {
    return number.toString(base);
  };
};
