const earthYearMap = new Map();
earthYearMap.set("mercury", 0.2408467);
earthYearMap.set("venus", 0.61519726);
earthYearMap.set("earth", 1);
earthYearMap.set("mars", 1.8808158);
earthYearMap.set("jupiter", 11.862615);
earthYearMap.set("saturn", 29.447498);
earthYearMap.set("uranus", 84.016846);
earthYearMap.set("neptune", 164.79132);

const earthYearSeconds = 31557600;

export function age(planet: String, seconds: number): number {
  return Number((seconds / (earthYearMap.get(planet.toLowerCase()) * earthYearSeconds)).toFixed(2))
}
