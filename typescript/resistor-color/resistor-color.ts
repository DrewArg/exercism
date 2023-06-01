export const COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
];

export const colorCode = (color: String): number => {
  const colorMap = new Map();
  for (let i = 0; i < COLORS.length; i++) {
    colorMap.set(COLORS[i].toString(), i);
  }

  return colorMap.get(color);
};
