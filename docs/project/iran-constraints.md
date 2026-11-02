# Iran Constraints

> **Status:** Living document · **Last reviewed:** 2026-11-02
> Filtering, sanctions, and regulations change often. Re-verify every item when the related decision is made. Legal items require confirmation by a local expert.

## 1. Connectivity

- Many foreign platforms are filtered (for example Instagram, Telegram, YouTube, X). Many users use VPNs, but the website must not rely on that.
- International connectivity has been severely restricted or shut down nationwide at times (for example November 2019, during the 2022 protests, June 2025), while domestically hosted services generally stayed reachable via the National Information Network (شبکه ملی اطلاعات).
- Mobile traffic is significant and bandwidth and latency vary.

**Implications:**
- Host inside Iran (DEC-018) so the site stays reachable during disruptions.
- No runtime dependency on foreign-hosted resources (fonts, CDNs, scripts, embeds, captchas, analytics) unless approved in `decisions.md`. Google Maps is an approved exception (DEC-022) and may not load without a VPN; Neshan, Balad, and a static fallback still cover the location. Requests to blocked domains can also stall page loading.
- If the English audience is outside Iran, check reachability and speed from abroad too (DEC-002).

## 2. Sanctions and Foreign Services

- Many foreign providers restrict Iranian users or IP addresses (for example several Google developer services and Docker Hub). Others are available under licenses (for example GitHub since 2021).
- International cards are not available, which makes paying for foreign SaaS difficult.
- Tools in the workflow (Figma, Cursor, GitHub, package registries) may be restricted or filtered, and their status can change.

**Checklist for every external service** (record results in the related decision):
1. Reachable from Iranian networks without VPN?
2. Can the center sign up and pay?
3. Behavior during an international disruption: does it fail gracefully?
4. Is there an Iranian or self-hosted alternative?
5. Is the data location acceptable?

## 3. Hosting and Infrastructure

Candidates to evaluate (examples, not decisions): Iranian cloud and PaaS providers such as ArvanCloud (ابر آروان), Liara (لیارا), Hamravesh (هم‌روش), ParsPack (پارس‌پک), and hosting companies such as Asiatech and Afranet.

Evaluation points: reachability inside and outside Iran; static hosting, object storage, and CDN options; deployment by CLI or API from CI; container registry mirrors; backups; SSL; pricing in Rial; support.

## 4. Domain, DNS, and SSL

- `.ir` domains are registered through IRNIC (nic.ir) or its resellers and require Iranian identity details.
- Foreign registrars commonly refuse Iranian customers; international TLDs obtained through intermediaries carry suspension risk.
- The registrant should be the legal business owner; eNamad checks domain ownership (verify).
- SSL via Let's Encrypt or the hosting provider.
- The brand name is Karoandishe and does not contain "LEGO" (DEC-012). A logo or a domain still needs the trademark check (DEC-019 for the domain).

## 5. Legal and Regulatory (Verify with a Local Expert)

- **Samandehi (ساماندهی):** registration of Iranian websites; confirm whether it applies.
- **eNamad (نماد اعتماد الکترونیکی):** required by most payment gateways (Phase 4); prerequisites include business documents and verified contact details.
- **Children's images:** photos, videos, and children's project work may be published publicly only after the necessary permissions have been obtained (DEC-013).
- **Online sales:** invoicing and tax obligations (Phase 4).
- **Personal data:** collect the minimum; store in Iran.

## 6. Localization

| Topic | Consideration |
|---|---|
| Language and direction | Persian, RTL; `lang="fa" dir="rtl"` |
| Digits | Persian digits (۰–۹) in the Persian UI; accept Persian, Arabic, and Latin digits in inputs |
| Text | Normalize ي/ك to ی/ک; preserve نیم‌فاصله (ZWNJ) |
| Calendar | Solar Hijri (Jalali) dates; week starts on Saturday; Friday is the weekend; official holidays include lunar dates that shift every year |
| Time zone | Asia/Tehran, UTC+03:30; daylight saving time abolished from 2023 — keep time zone data up to date |
| Currency | Display is Toman; formats are in DEC-015. Rial is official (10 Rials = 1 Toman). A redenomination has been in the legislative process — verify; inflation causes frequent price changes |
| Phone numbers | Mobile `09xx xxx xxxx` / `+98 9xx xxx xxxx`; landlines with area codes |
| Addresses | Persian address format; 10-digit postal code |
| Fonts | Persian: Vazirmatn. Latin: Inter. Both are self-hosted, not loaded from a font service (DEC-023) |

## 7. Third-Party Services by Area

| Area | Concern | Options to evaluate | Phase |
|---|---|---|---|
| Maps | Google Maps Platform requires international billing; availability varies, and it may not load in Iran without a VPN | Decided (DEC-022): Google Maps, Neshan (نشان), and Balad (بلد), plus a static fallback. Neshan and Balad cover visitors without a VPN | 1 |
| Analytics | Foreign tools may be unreliable to load or manage from Iran; data stored abroad | Self-hosted analytics (e.g., Umami, Matomo) on Iranian hosting; Iranian services | 1 |
| Video | YouTube filtered | Direction, not decided (DEC-011): Aparat (آپارات), and possibly self-hosted storage | 1 |
| Social and messaging | Instagram is filtered. The channels to display are Instagram (a link only), an Aparat channel, and SMS (DEC-010). The phone number, SMS number, and Instagram and Aparat addresses are set in the Figma designs (T1.2.2.2). This does not decide video hosting (DEC-011) | Linking filtered platforms is allowed; visitors use their own VPN. Do not embed them | 1 |
| Spam protection | Google reCAPTCHA unreliable | Honeypot fields, rate limiting, self-hosted captcha | 1 |
| Fonts and CDNs | Foreign font services and public CDNs may be slow or blocked | Self-host all assets | 1 |
| Email | Deliverability from Iranian servers to international mailbox providers may be poor | Test deliverability; consider SMS or messaging notifications | 1, 3 |
| SMS | — | Iranian providers, e.g., Kavenegar, Ghasedak, SMS.ir | 3 |
| Payments | International gateways unavailable | Shaparak PSP gateways; payment facilitators (e.g., Zarinpal, Zibal) | 4 |

## 8. Development and Delivery

- GitHub is accessible. CI runners hosted abroad may fail to deploy to Iranian hosts during disruptions or when hosts block foreign traffic. Options: provider CLI/API deployment, a self-hosted runner inside Iran, or an Iranian Git/CI platform (DEC-020).
- npm is generally reachable; Docker Hub is restricted, and Iranian mirrors exist.
- Keep local backups of Figma files and a mirror of the repository.
- Some AI and developer tools may require a VPN — a schedule risk.

## 9. Testing

- Test without VPN on mobile operators (همراه اول, ایرانسل, رایتل) and fixed-line ISPs (for example مخابرات, شاتل, آسیاتک, پارس آنلاین, مبین‌نت).
- Android is expected to dominate the device mix (verify with analytics); include mid-range and older Android devices and iOS Safari.
- Simulate foreign-blocked conditions by blocking third-party domains in browser developer tools.
- Monitor uptime from inside and outside Iran.
- Who tests from Iranian networks and on which devices: DEC-034. Automated checks for foreign requests and the test approach: [testing-strategy.md §4.10](../testing/testing-strategy.md#410-iran-network-and-resilience-testing).

## 10. Payments (Phase 4)

- All online card payments go through Shaparak, via a direct PSP gateway or a payment facilitator.
- Gateways typically require eNamad and business documents, and often an Iranian server IP.
- No card data should touch the platform; payment is completed on the gateway's page and verified server-side.
- Details: [phase-4-payment.md](../phases/phase-4-payment.md).
