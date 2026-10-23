// Crate Math engine: the crates an item load packs, the weight and trips, the cost an item, and the minutes the load packs. Exact integers, half-up on display only. No named constants; every number is the owner's own entry.
function _i(t, err, digits, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  if (!new RegExp("^[0-9]{1," + digits + "}$").test(t)) throw new Error(err);
  var v = parseInt(t, 10);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _p(t, err, intDigits, places, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  var m = new RegExp("^([0-9]{1," + intDigits + "})(?:\\.([0-9]{1," + places + "}))?$").exec(t);
  if (!m) throw new Error(err);
  var v = parseInt(m[1], 10) * Math.pow(10, places) + (m[2] ? parseInt(m[2].padEnd(places, "0"), 10) : 0);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _m(v) {
  var w = Math.floor(v / 100), f = String(v % 100).padStart(2, "0");
  return w + "." + f;
}
function _pl(n, one, many) { return n + (n === 1 ? one : many); }
function _v(n, one, many) { return n === 1 ? one : many; }
var _IT = "the items must be from 1 to 1000000 with no decimal places";
var _IC = "the items a crate must be from 1 to 10000 with no decimal places";
var _CR = "the crates must be from 1 to 100000 with no decimal places";
var _KG = "the kilograms a crate must be from 1 to 1000 with no decimal places";
var _TR = "the kilograms a trip must be from 1 to 100000 with no decimal places";
var _PR = "the crate price must be from 0.01 to 999.99 with up to 2 decimal places";
var _IM = "the items a minute must be from 1 to 1000 with no decimal places";

function cratesTruth(items, perCrate) {
  var n = _i(items, _IT, 7, 1, 1000000), c = _i(perCrate, _IC, 5, 1, 10000);
  var k = Math.floor((n + c - 1) / c), last = n - (k - 1) * c;
  return "The " + _pl(n, " item", " items") + " at " + _pl(c, " item", " items") + " a crate " + _v(n, "makes", "make") + " " + _pl(k, " crate", " crates") + ", the last crate covering " + _pl(last, " item", " items") + ".";
}
function weightTruth(crates, kgCrate, kgTrip) {
  var k = _i(crates, _CR, 6, 1, 100000), w = _i(kgCrate, _KG, 4, 1, 1000), v = _i(kgTrip, _TR, 6, 1, 100000);
  var t = k * w, trips = Math.floor((t + v - 1) / v), last = t - (trips - 1) * v;
  return "The " + _pl(k, " crate", " crates") + " at " + _pl(w, " kilogram", " kilograms") + " a crate " + _v(k, "weighs", "weigh") + " " + _pl(t, " kilogram", " kilograms") + ", " + _pl(trips, " trip", " trips") + " at " + _pl(v, " kilogram", " kilograms") + " a trip, the last trip carrying " + _pl(last, " kilogram", " kilograms") + ".";
}
function costTruth(crates, price, items) {
  var k = _i(crates, _CR, 6, 1, 100000), p = _p(price, _PR, 3, 2, 1, 99999), n = _i(items, _IT, 7, 1, 1000000);
  var cc = k * p;
  var pi = Math.floor((2 * cc + n) / (2 * n));
  return "The " + _pl(k, " crate", " crates") + " at $" + _m(p) + " a crate " + _v(k, "comes", "come") + " to $" + _m(cc) + ", $" + _m(pi) + " an item.";
}
function timeTruth(items, perMinute) {
  var n = _i(items, _IT, 7, 1, 1000000), m = _i(perMinute, _IM, 4, 1, 1000);
  var t = Math.floor((n + m - 1) / m), h = Math.floor(t / 60), r = t % 60;
  return "The " + _pl(n, " item", " items") + " at " + _pl(m, " item", " items") + " a minute " + _v(n, "takes", "take") + " " + _pl(t, " minute", " minutes") + ", " + _pl(h, " hour", " hours") + " " + _pl(r, " minute", " minutes") + ".";
}
