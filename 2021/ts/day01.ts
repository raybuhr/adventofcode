import { readFileSync } from 'fs';

const rawData = readFileSync('data.txt', 'utf-8');

function parseData(rawData: string) {
    let lines = rawData.split('\n');
    let sequence = lines.map(i => parseInt(i));
    return sequence
}

function partOne(sequence: number[]) {
    let count = 0;
    for (let i = 1; i < sequence.length; i++) {
        if (sequence[i] > sequence[i-1]) {
            count += 1;
        }
    }
    return count;
}

function partTwo(sequence: number[]) {
    let count = 0;
    let window: number[] = []
    for (let i = 2; i < sequence.length; i++) {
        let current = sequence[i-2] + sequence[i-1] + sequence[i];
        window.push(current);
    }
    for (let i = 1; i < window.length; i++) {
        if (window[i] > window[i-1]) {
            count += 1;
        }
    }
    return count;
}


let data = parseData(rawData)

console.log("Part One")
let partOneAnswer = partOne(data)
console.log(partOneAnswer)

console.log("Part Two")
let partTwoAnswer = partTwo(data)
console.log(partTwoAnswer)
