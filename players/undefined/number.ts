import superagent from 'superagent';

function sleep(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
    const res = await superagent.post('http://202.38.93.141:12122/game')
        .set('Content-Type', 'application/json')
        .send({})
        .set('Cookie', '[redacted]');
    console.log(res.body);
    const r: string[] = [];
    for (const t of res.body.values) {
        if (t[0] > t[1]) r.push('>')
        else if (t[0] < t[1]) r.push('<')
        else r.push('=')
    }
    console.log(r.join(''));
    await sleep(5000);
    const t = await superagent.post('http://202.38.93.141:12122/submit')
        .send({ inputs: r })
        .set('Content-Type', 'application/json')
        .set('Cookie', '[redacted]');
    console.log(t.body);
}

main();