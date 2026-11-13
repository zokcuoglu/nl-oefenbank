// Woordle results for NL Oefenbank (same documents as Slimspel writes; see firestore.rules: woordle_plays).
// Kept out of core.js on purpose: browsers may still have an older core.js in their cache for a few minutes,
// and a page that asks core.js for a function it does not have yet stops loading completely.
import { db } from "./core.js";
import { doc, setDoc, collection, getDocs, query, where } from "https://www.gstatic.com/firebasejs/12.19.0/firebase-firestore.js";

// One document per person, language, level and day: { uid, name (first name), lang, level, day, won, guesses, time_s, at }
export function saveWoordlePlay(user, profile, play) {
  if (profile._view) return Promise.resolve();   // admin in "view as": nothing is written
  const name = (profile.name || user.displayName || "?").trim().split(/\s+/)[0];
  return setDoc(doc(db, "woordle_plays", `${play.lang}-${play.level}-${play.day}-${user.uid}`), {
    uid: user.uid, name: name.slice(0, 40), lang: play.lang, level: play.level, day: play.day,
    won: !!play.won, guesses: Math.round(play.guesses), time_s: Math.max(0, Math.round(play.time_s)), at: new Date().toISOString()
  });
}
// Everyone's Woordle results from `fromDay` (YYYY-MM-DD) on
export async function loadWoordlePlays(fromDay) {
  const snap = await getDocs(query(collection(db, "woordle_plays"), where("day", ">=", fromDay)));
  return snap.docs.map(d => d.data());
}
