use sha2::{Sha256, Digest};
use rand::{rngs::ThreadRng, thread_rng, Rng};
use std::collections::HashMap;
use std::thread;
use std::sync::Arc;
use std::sync::Mutex;
use std::time::Duration;

fn random_array(rng: &mut ThreadRng) -> [u8; 8] {
    let value: [u8; 8] = rng.gen();
    value
}

fn sha256_hash(data: [u8; 8]) -> u32 {
    let mut hasher = Sha256::new();
    hasher.update(data);
    let result = hasher.finalize();
    let len = result.len();
    let v = 
                (result[len - 4] as u32) << 24 |
                (result[len - 3] as u32) << 16 |
                (result[len - 2] as u32) << 8 |
                (result[len - 1] as u32) << 0;
    v
}

fn find_hash(result: Arc<Mutex<[u8; 8]>>, count: Arc<Mutex<usize>>, target_hash: u32) {
    let mut local_cnt: usize = 0;
    let mut rng = thread_rng();
    loop {
        let data = random_array(&mut rng);
        let hash = sha256_hash(data);
        if hash == target_hash {
            println!("Found: {} with hash {}", hex::encode(data), hash);
            'tryset: loop {
                let mut guard = match result.lock() {
                    Ok(guard) => guard,
                    Err(_) => {
                        thread::sleep(Duration::from_millis(200));
                        continue 'tryset;
                    }
                };
                *guard = data;
                return;
            }
        }

        local_cnt += 1;
        if local_cnt % 10000 == 0 {
            let mut guard = match count.lock() {
                Ok(guard) => guard,
                Err(_) => {
                    continue;
                }
            };
            *guard += 10000;
        }
    }
}

fn main() {
    let mut tests: usize = 0;
    let mut rng = thread_rng();
    let mut map = HashMap::<u32, [u8; 8]>::new();
    let (data1, data2, hash) = loop {
        let data = random_array(&mut rng);
        let hash = sha256_hash(data);
        if let Some(x) = map.get(&hash) {
            println!("Found: {} {} with hash {}", hex::encode(data), hex::encode(x), hash);
            break (data, x.clone(), hash);
        }
        map.insert(hash, data);
        tests += 1;
        if tests % 10000 == 0 {
            println!("Tested: {},", tests)
        }
    };
    let result = Arc::new(Mutex::new([0 as u8; 8]));
    let count = Arc::new(Mutex::new(0 as usize));
    let mut threads = vec![];
    for _ in 0..16 {
        let result_h = result.clone();
        let count_h = count.clone();
        let handler = thread::spawn(move || {
            find_hash(result_h, count_h, hash);
        });
        threads.push(handler);
    }
    let data3 = loop {
        {
            let guard = match result.try_lock() {
                Ok(g) => g,
                Err(_) => {
                    thread::sleep(Duration::from_millis(100));
                    continue;
                }
            };
            if *guard != [0; 8] {
                break *guard;
            }
        }
        {
            let guard = match count.try_lock() {
                Ok(g) => g,
                Err(_) => {
                    thread::sleep(Duration::from_millis(100));
                    continue;
                }
            };
            println!("Tested: {}", *guard)
        }
        thread::sleep(Duration::from_millis(250));
    };
    println!("Found: {} {} {} with hash {}", hex::encode(data1), hex::encode(data2), hex::encode(data3), hash);
}
