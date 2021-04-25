fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input = std::fs::read_to_string("../input.txt")?
        .lines()
        .map(|x| x.parse::<u32>())
        .collect::<Result<Vec<u32>, std::num::ParseIntError>>()?;
    Ok(println!(
        "{:?}",
        input
            .iter()
            .filter(|x| input.iter().any(|y| *x != y && *x + *y == 2020))
            .fold(1, |x, y| x * *y)
    ))
}
