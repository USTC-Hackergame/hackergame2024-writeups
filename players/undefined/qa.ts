import superagent from "superagent";

async function main() {
    for (let i = 1; ; i++) {
        const res = await superagent.post(`http://202.38.93.141:13030/`)
            .send({
                q1: "3A204",
                q2: "2682",
                q3: "程序员的自我修养",
                q4: 336,
                q5: "6e90b6",
                q6: "1833",
            })
            .type('form')
            .set('Cookie', `[REDACTED]`)
        if (!res.text.includes('本次测验总得分为 90')) {
            console.log(`res=${i} ${res.text}`);
            break;
        }
        else if (!(i % 10)) console.log(`res=${i} ${res.text.split('本次测验总得分为 ')[1].substring(0, 2)}`);
    }
}

main(); 