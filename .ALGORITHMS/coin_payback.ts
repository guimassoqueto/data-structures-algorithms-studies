// function getTroco(price: number, client: number): Array<number> {
//     type coin_type = 1 | 5 | 10 | 25 | 50;
//     let troco_centavos = Math.round((client - price) % 1 * 100);

//     function count_coins_payback(troco_centavos: number, coin: coin_type): [number, number] {
//         let coin_count = 0; 
//         while(troco_centavos >= coin) {
//             troco_centavos -= coin;
//             coin_count++;
//         }
//         return [coin_count ? coin_count : 0, troco_centavos % coin];
//     }

//     const [fifty_coins, fifty_left] = count_coins_payback(troco_centavos, 50)
//     const [twenty_five_coins, twenty_five_left] = count_coins_payback(fifty_left, 25)
//     const [ten_coins, ten_left] = count_coins_payback(twenty_five_left, 10)
//     const [five_coins, five_left] = count_coins_payback(ten_left, 5)
//     const [one_coins, one_left] = count_coins_payback(five_left, 1)

//     return [fifty_coins, twenty_five_coins, ten_coins, five_coins, one_coins];
// }

type Coins = {
    [key: number]: number
}

class CoinCounter {
    public accepted_coins: number[] = [];

    addCoin(coin_value: number) {
        this.accepted_coins.push(coin_value);
        this.accepted_coins.sort((n1: number, n2: number) => n2 - n1)
    }

    calc_payback(product_price: number, customer_money: number) {
        let payback = Math.round((customer_money - product_price) % 1 * 100);
        let coins_count: Coins = {};
        for (const coin of this.accepted_coins) {
            let coin_count: number = 0;
            while(payback >= coin) {
                payback -= coin;
                coin_count++;
            }
            coins_count[coin] = coin_count;
        }
        console.log(coins_count);
    }
}

