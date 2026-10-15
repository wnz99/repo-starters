export function normalizeName(value: string): string {
  const name = value.trim();
  if (name.length === 0) throw new Error("Name is required");
  return name;
}
