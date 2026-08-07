from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power),
        )
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    test_values = [21, 10, 5]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def shield(target: str, power: int) -> str:
        return f"Shield blocks {target}'s attack for {power} damage"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined(test_targets[0], test_values[0])
    print(f"Combined spell result: {result1}, {result2}")
    print("\nTesting power amplifier...")

    def simple_fireball(target: str, power: int) -> int:
        return power

    mega_fireball = power_amplifier(simple_fireball, 3)
    print(
        f"Original: {test_values[0]}, "
        f"Amplified: {mega_fireball(test_targets[0], test_values[0])}"
    )

    print("\nTesting conditional caster...")

    def enough_power(target: str, power: int) -> bool:
        return power >= 10

    safe_fireball = conditional_caster(enough_power, fireball)

    print(safe_fireball(test_targets[0], test_values[0]))
    print(safe_fireball(test_targets[1], test_values[1]))

    print("\nTesting spell sequence...")

    combo = spell_sequence([
        fireball,
        heal,
        shield
    ])

    results = combo(test_targets[2], test_values[2])

    for result in results:
        print(result)
